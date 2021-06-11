import cx_Freeze
executables = [cx_Freeze.Executable(script="game.py", icon="assets/alekicone.ico")]

cx_Freeze.setup(
    name="Não deixe o Alek morrer",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files":["assets"]
    }},
    executables = executables
)
