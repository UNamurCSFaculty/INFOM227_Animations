# INFOM227 Animations

INFOM277 Animations contains the code to generate animations for the course INFOM227.

- **Downloads page:** https://github.com/UNamurCSFaculty/INFOM227_Animations/releases

## Requirements

The application requires:

- [Python](https://www.python.org/) ~= 3.11
- [pip](https://pip.pypa.io/en/stable/)

## Download & Installation

There are two ways to download and install the application:

### Using Git

You can install the application using Git by running the following command:

```bash
pip install git+https://github.com/UNamurCSFaculty/INFOM227_Animations.git
```

### Using the GitHub releases

You can download the application on the [downloads page](https://github.com/UNamurCSFaculty/INFOM227_Animations/releases). Then, you can install the application by running the following command:

```bash
pip install infom227_animations-X.X.X-py3-none-any.whl
```

(Note: The X.X.X must be replaced by the version that you want to install.)

## Usage

You can generate an animation by running the following command:

```bash
manim render <path-to-the-scene-file>
```

The scenes are stored in the [scenes.py](https://github.com/UNamurCSFaculty/INFOM227_Animations/blob/main/scenes.py) file.

### Example

```bash
manim render scenes.py SimpleIfZeroAnalysisScene
```

## License

All code is licensed for others under a MIT license (see [LICENSE](https://github.com/UNamurCSFaculty/INFOM227_Animations/blob/main/LICENSE)).
