import marimo

__generated_with = "0.10.12"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("""# Welcome to marimo on fly.io! 🚀""")
    return


@app.cell
def _(mo):
    slider = mo.ui.slider(1, 100, value=50)
    slider
    return (slider,)


@app.cell
def _(mo, slider):
    mo.md(f"## The current value is: {slider.value}")
    return


if __name__ == "__main__":
    app.run()
