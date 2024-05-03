# Setting Up WeasyPrint in Pycharm (Mac OS) (2023)

This guide helps you troubleshoot and resolve the "unable to find dependencies" error when using WeasyPrint in PyCharm on Mac OS, specifically when Homebrew is installed but not linked to PyCharm.

**Problem:** You've installed Homebrew and WeasyPrint, but encounter errors like:
```
OSError: cannot load library 'gobject-2.0-0': dlopen(gobject-2.0-0, 0x0002): tried: 'gobject-2.0-0' (no such file), '/System/Volumes/Preboot/Cryptexes/OSgobject-2.0-0' (no such file), '/usr/lib/gobject-2.0-0' (no such file, not in dyld cache), 'gobject-2.0-0' (no such file), '/opt/homebrew/opt/gobject-introspection/gobject-2.0-0' (no such file). Additionally, ctypes.util.find_library() did not manage to locate a library called 'gobject-2.0-0'
```

**Cause:** Your Python interpreter in PyCharm isn't configured to use the Homebrew installation path.

**Solution:**

1. **Identify Homebrew Path:**
    * Open terminal and run `brew --prefix`. The output (e.g., `/opt/homebrew`) is your Homebrew path.
    * Verify Python installation:
        ```
        cd /opt/homebrew/bin
        ls # This should show a Python3 installation
        ```

2. **Configure PyCharm Interpreter:**
    * Create a new PyCharm project.
    * Go to Preferences > Project > Python Interpreter.
    * Click the gear icon and select "Add."
    * Choose "Local..." and paste the Homebrew Python path (e.g., `/opt/homebrew/bin/python3`).
    * Save the changes.

Now you should be able to use WeasyPrint and other Homebrew libraries in your PyCharm project!
