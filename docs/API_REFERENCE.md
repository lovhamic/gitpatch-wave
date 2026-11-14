# API Reference

This document provides technical documentation for the HTTP endpoints exposed by GitPatch Wave.

## Base URL

When running locally in development mode, the base URL is:

```
http://127.0.0.1:8080
```

## Endpoints

### 1. Introduction Screen

Renders the landing splash page with animated starfield and interactive particle trails.

- **URL**: `/`
- **Method**: `GET`
- **Headers**: `Accept: text/html`
- **Response**: `200 OK` (HTML document)

---

### 2. Plotter Workspace

Renders the primary wave visualization and parameter configuration interface.

- **URL**: `/plotter`
- **Method**: `GET`
- **Headers**: `Accept: text/html`
- **Response**: `200 OK` (HTML document)

---

### 3. Calculate Wave

Computes discrete coordinates for one or more mathematical wave equations across a specified domain, along with the composite superposition curve.

- **URL**: `/calculate_wave`
- **Method**: `GET`
- **Headers**: `Accept: application/json`

#### Query Parameters

| Parameter | Type | Required | Default | Description |
| --------- | ---- | -------- | ------- | ----------- |
| `minX` | `float` | No | `-15` | Minimum bound of the horizontal evaluation domain. |
| `maxX` | `float` | No | `15` | Maximum bound of the horizontal evaluation domain. |
| `t` | `float` | No | `0` | Time parameter used in time-dependent wave functions. |
| `eq0` | `string` | No | None | First mathematical wave equation. |
| `eq1` | `string` | No | None | Second mathematical wave equation (additional equations follow pattern `eq2`, `eq3`, etc.). |
| `[varName]` | `float` | No | None | Dynamic numerical value for any custom variable referenced in equations (e.g., `A=1.5`, `k=2.0`, `w=0.5`). |

#### Supported Mathematical Functions and Constants

| Identifier | Description | NumPy Mapping |
| ---------- | ----------- | ------------- |
| `sin(x)` | Sine function | `numpy.sin` |
| `cos(x)` | Cosine function | `numpy.cos` |
| `tan(x)` | Tangent function | `numpy.tan` |
| `exp(x)` | Natural exponential ($e^x$) | `numpy.exp` |
| `sqrt(x)` | Square root | `numpy.sqrt` |
| `abs(x)` | Absolute value | `numpy.abs` |
| `log(x)` | Natural logarithm | `numpy.log` |
| `log10(x)` | Base-10 logarithm | `numpy.log10` |
| `pi` | Circle ratio constant ($\pi \approx 3.14159$) | `numpy.pi` |
| `e` | Euler's number ($e \approx 2.71828$) | `numpy.e` |
| `x` | Evaluation domain vector | Array of 1,000 float points |
| `t` | Time parameter scalar | Float passed in query string |
| `^` | Power operator (converted to `**`) | Python exponentiation |

#### Successful Response (`200 OK`)

Returns a JSON object with evaluation vectors:

```json
{
  "x": [-10.0, -9.98, "...1000 items...", 10.0],
  "lines": [
    [0.544, 0.528, "...1000 items...", -0.544],
    [-0.839, -0.849, "...1000 items...", -0.839]
  ],
  "superposition": [-0.295, -0.321, "...1000 items...", -1.383]
}
```

##### Response Fields

- **`x`** (`array[float]`): Monotonically increasing array of 1,000 sampling points between `minX` and `maxX`.
- **`lines`** (`array[array[float]]`): List of evaluated y-coordinates for each provided equation, in ascending lexicographical order of equation keys (`eq0`, `eq1`, ...).
- **`superposition`** (`array[float]`): Point-by-point sum of all computed lines across the domain.

#### Error Response (`200 OK` with error key)

If an invalid expression or unresolvable variable is supplied, an error object is returned:

```json
{
  "error": "name 'omega' is not defined"
}
```

#### Example Requests

##### Single Sine Wave
```
GET /calculate_wave?t=0&eq0=sin(x)&minX=-10&maxX=10
```

##### Traveling Wave with Custom Variables
```
GET /calculate_wave?t=1.5&eq0=A*sin(k*x-w*t)&A=2.0&k=1.2&w=0.8&minX=-15&maxX=15
```

##### Superposition of Two Waves
```
GET /calculate_wave?t=0.5&eq0=sin(x-t)&eq1=0.5*cos(2*x-t)&minX=-10&maxX=10
```
