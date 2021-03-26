// Create a global manager with an auto-executable anonymous function.
var Commander = (function(scope) {
    'use strict';
  
    // Manager object instance.
    var obj = {};
  
    // -- Private --
  
    // Command list.
    var _commands = {};
    // Commands list for undo/redo.
    var _list = [];
    // Current command index on `list`.
    var _current = 0;
  
    var _currentCommand = function() {
      var name = _list[_current];
      return _commands[name];
    };
  
    // -- Public --
  
    // Add a new command to the list (name shortcut). `name` must be a string, and `command`
    // must be an object which responds to `execute` and `undo`.
    obj.addCommand = function(name, command) {
      _commands[name] = command;
    };
  
    // Execute a command by its name.
    obj.execute = function(name) {
      var cmd = _commands[name];
  
      // Remove the actions after `current` command in the stack. Of course,
      // if we undo 3 times, we can redo 3 times. However, if we undo 3 times,
      // and execute a new action, we can no longer those 3 old commands.
      // This action will not affect the list if the `current` points to the last element.
      _list = _list.slice(0, _current);
  
      // Execute the command, add it to the top of the stack and increment the current index.
      cmd.execute();
      _list.push(name);
      _current += 1;
    };
  
    // Check if the the next command can be `undone`
    obj.canUndo = function() {
      return _current > 0;
    };
  
    // Check if the next command can be `redone`.
    obj.canRedo = function() {
      return _current < _list.length;
    };
  
    // Undo the previous command executed.
    obj.undo = function() {
      // Stop if there are no elements on the list.
      if (!obj.canUndo()) return false;
  
      // Move back, and undo the previous command.
      _current -= 1;
      _currentCommand().undo();
      return true;
    };
  
    // Redo the next command.
    obj.redo = function() {
      // Stop if there are no elements on the list.
      if (!obj.canRedo()) return false;
  
      // Move forward, and execute the next command.
      _currentCommand().execute();
      _current += 1;
      return true;
    };
  
    // Restart commands list.
    obj.restart = function() {
      _list = [];
      _current = 0;
    };
  
    // Return the instance.
    return obj;
  })(window);