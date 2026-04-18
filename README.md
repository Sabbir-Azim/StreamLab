# StreamLab

<p align="center">
  <img src="streamlab-banner.png" alt="StreamLab banner" style="max-width:100%; height:auto;">
</p>

Render websites and YouTube videos directly inside IPython notebooks.

**StreamLab** is a lightweight Python package designed for notebook-first workflows. It makes it easy to display live websites and YouTube videos inside Jupyter, Google Colab, and other IPython-based environments without leaving your notebook.

---

## Why StreamLab?

When working in notebooks, it is often useful to keep external content close to your code, notes, demos, or experiments. StreamLab helps by embedding web pages and video content directly into notebook cells.

Use it for:

- interactive demos
- educational notebooks
- research presentations
- rapid prototyping
- media-rich documentation
- dashboards and reference views inside notebooks

---

## Features

- Render **any website** inside an IPython notebook
- Embed **YouTube videos** directly in notebook output cells
- Simple API for notebook-based workflows
- Useful for both **Jupyter Notebook** and **Google Colab**
- Minimal setup and quick integration into existing projects

---

## Installation

Install from PyPI:

```bash
pip install streamlab
```

Or install the latest development version from GitHub:

```bash
pip install git+https://github.com/<your-username>/StreamLab.git
```

---

## Quick Start

> **Note:** Replace the example function names below with your actual public API if your implementation uses different names.

### Render a website

```python
from streamlab import render_website

render_website("https://example.com")
```

### Render a YouTube video

```python
from streamlab import render_youtube

render_youtube("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
```

### Use inside Jupyter / Colab

```python
from streamlab import render_website, render_youtube

render_website("https://pypi.org")
render_youtube("https://www.youtube.com/watch?v=VIDEO_ID")
```

---

## Example Use Cases

### 1. Notebook-based teaching
Show lecture resources, reference sites, or YouTube tutorials directly inside a notebook.

### 2. Data storytelling
Embed external dashboards, reports, or explainer videos alongside analysis.

### 3. Research workflows
Keep documentation pages, papers, or relevant web tools visible during experiments.

### 4. Product demos
Build richer notebooks by combining code, websites, and videos in a single place.

---

## Supported Environments

StreamLab is intended for environments that support IPython display capabilities, including:

- Jupyter Notebook
- JupyterLab
- Google Colab
- Other IPython-based notebook environments

Behavior may vary depending on browser security settings, iframe restrictions, or third-party site policies.

---

## Notes and Limitations

- Some websites may block embedding through iframe or browser security headers.
- YouTube embedding behavior may depend on regional, browser, or policy restrictions.
- Notebook environments may render external content differently depending on frontend support.

If a site does not render, the issue may be caused by the target website rather than StreamLab itself.

---

## API Design Idea

If you want a simple public API, you may expose functions such as:

```python
render_website(url: str, width: int = 900, height: int = 500)
render_youtube(url: str, width: int = 900, height: int = 500)
```

If your package already uses different function names or parameters, update this section accordingly.

---

## Roadmap

Possible future improvements:

- custom width and height controls
- support for more video platforms
- URL validation helpers
- better fallback messages for blocked sites
- richer notebook widget integration
- theme-aware rendering options

---

## Contributing

Contributions are welcome.

If you would like to improve StreamLab, feel free to:

1. fork the repository
2. create a feature branch
3. make your changes
4. submit a pull request

Bug reports, feature requests, and feedback are always appreciated.

---

## License

Add your preferred license here.

Example:

```text
MIT License
```

If you plan to publish on PyPI, make sure the license in this README matches your repository and package metadata.

---

## Author

**Your Name**  
GitHub: [@your-username](https://github.com/<your-username>)

---

## Project Status

StreamLab is under active development. The API may evolve as the project grows.
