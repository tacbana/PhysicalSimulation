# Copilot Instructions for Physical Simulation Project

## Architecture Overview

This is a PyQt5-based GUI application for physics simulation demonstrations. The main application (`Physical_Simulation.py`) provides a central hub with domain buttons (力学, 热学, etc.), each leading to simulation options that open in separate dialog windows.

Key components:

- **Main App**: `SimulationApp` class manages the main window and simulation selection
- **Simulation Frames**: Each physics simulation is a separate module (e.g., `Three_Body_Frame.py`, `movement_air_frame.py`) containing a frame class that inherits from a base widget
- **UI Files**: Qt Designer `.ui` files in `ui/` folder, with some converted to Python in `_ui.py` files
- **AI Integration**: Ollama subprocess for chat functionality in `AIChatDialog`

## Critical Workflows

- **Run Application**: `python Physical_Simulation.py` (requires PyQt5 and ollama installed)
- **Add New Simulation**: Create a new module with a frame class, add to `simulation_options` dict in `SimulationApp.__init__`, and implement `add_*_tab` method following the pattern in `add_simulation_window`
- **Update UI**: Edit `.ui` files in `ui/` folder, regenerate `_ui.py` if needed
- **Debug AI Chat**: Check ollama output in console; uses subprocess with UTF-8 encoding

## Project Conventions

- **Naming**: Simulation modules use snake_case (e.g., `three_body_frame.py`), frame classes use PascalCase (e.g., `three_body_frame`)
- **Language**: Chinese strings for UI elements and comments
- **Imports**: All simulation frames imported at top of `Physical_Simulation.py`
- **Dialog Pattern**: Simulations open in `QDialog` with `QVBoxLayout` containing the frame widget, minimum size 900x700
- **Styling**: Buttons use custom CSS with rounded corners, hover effects, and domain-specific icons from PNG files

## Integration Points

- **Ollama AI**: Subprocess call to `ollama run codellama:latest` for chat responses; handles ANSI codes and spinners in output
- **Qt Signals**: Use `pyqtSignal` for thread communication in `AIWorker` class
- **Threading**: AI responses processed in background `QThread` to avoid UI blocking

## Examples

- Adding a new domain: Update `simulation_options` dict and create corresponding `add_*_tab` method
- Frame Class Structure: See `Three_Body_Frame.py` - class inherits from QWidget, implements simulation logic and UI updates
- Icon Assignment: Domain buttons use icons from root directory (e.g., `mechanics_icon.png`)
