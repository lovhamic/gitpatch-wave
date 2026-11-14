from flask import Flask, render_template, jsonify, request
import numpy as np
import os
import sys
import webbrowser
from threading import Timer

# --- 1. PATH HANDLING FOR PYINSTALLER ---
def resource_path(relative_path):
    """Get absolute path to resource, works for development and PyInstaller bundles."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

# --- 2. FLASK APP SETUP ---
app = Flask(
    __name__,
    template_folder=resource_path('templates'),
    static_folder=resource_path('static')
)

# Mathematical functions and constants available for equations
ALLOWED_MATH = {
    "sin": np.sin, "cos": np.cos, "tan": np.tan,
    "exp": np.exp, "sqrt": np.sqrt, "pi": np.pi,
    "abs": np.abs, "log": np.log, "log10": np.log10, "e": np.e
}

# --- 3. ROUTES ---
@app.route('/')
def intro():
    """Render the animated splash and introduction page."""
    return render_template('intro.html')

@app.route('/plotter')
def plotter():
    """Render the main interactive wave plotter interface."""
    return render_template('index.html')

@app.route('/calculate_wave')
def calculate_wave():
    """
    Calculate discrete wave points and superposition for given equations and parameters.
    
    Query parameters:
    - minX (float): Minimum bound of x domain (default: -15).
    - maxX (float): Maximum bound of x domain (default: 15).
    - t (float): Time parameter (default: 0).
    - eq0, eq1, ... (str): Wave mathematical expressions.
    - Custom variable names (float): Numerical values for named variables.
    
    Returns:
    - JSON object containing x array, individual line evaluations, and superposition sum.
    """
    try:
        args = request.args.to_dict()
        min_x = float(args.pop('minX', -15))
        max_x = float(args.pop('maxX', 15))
        t_val = float(args.pop('t', 0))
        
        x = np.linspace(min_x, max_x, 1000)

        # Separate equations (eq0, eq1...) from variables
        equations = {k: v for k, v in args.items() if k.startswith('eq')}
        for k in equations:
            args.pop(k)

        # Setup evaluation context
        safe_dict = ALLOWED_MATH.copy()
        safe_dict['x'] = x
        safe_dict['t'] = t_val
        
        # Add custom variables (e.g., A, k, w) to the math evaluation context
        for key, value in args.items():
            try:
                # Ensure core math functions are not overwritten
                if key not in ALLOWED_MATH:
                    safe_dict[key] = float(value)
            except (ValueError, TypeError):
                pass

        results = []
        total_y = np.zeros_like(x)
        
        for key in sorted(equations.keys()):
            clean_eq = equations[key].replace("^", "**")
            # Evaluate using restricted math context
            y = eval(clean_eq, {"__builtins__": None}, safe_dict)
            
            if isinstance(y, (int, float)):
                y = np.full_like(x, y)
            results.append(y.tolist())
            total_y += y 

        return jsonify({
            "x": x.tolist(),
            "lines": results, 
            "superposition": total_y.tolist()
        })
    except Exception as e:
        return jsonify({"error": str(e)})

# --- 4. BROWSER AUTO-OPENER ---
def open_browser(url):
    """Open default system web browser to the application URL."""
    webbrowser.open_new(url)

if __name__ == '__main__':
    host = os.environ.get('HOST', '127.0.0.1')
    port = int(os.environ.get('PORT', 8080))
    no_browser = os.environ.get('NO_BROWSER', '').lower() in ('1', 'true', 'yes')

    if not no_browser and host in ('127.0.0.1', 'localhost'):
        target_url = f'http://{host}:{port}/'
        Timer(1.5, open_browser, args=[target_url]).start()

    app.run(host=host, port=port, debug=False)
