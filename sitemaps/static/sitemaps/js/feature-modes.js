
 
const DrawNamedLineMode = {};
const DrawLineString = MapboxDraw.modes.draw_line_string;

Object.assign(DrawNamedLineMode, DrawLineString, {

isNameRequired: true,
showNamePrompt: true,

    onSetup: function(opts) {
        const state = DrawLineString.onSetup.call(this, opts);
        const isNameRequired = this.isNameRequired === true;
        const featureName = opts.featureName;
        const showNamePrompt = (opts.showNamePrompt !== undefined ? opts.showNamePrompt === true : this.showNamePrompt === true) || (isNameRequired && !featureName);
        const extendedState = Object.assign(state, {
            isNameRequired: isNameRequired,
            name: featureName
        });
        if (showNamePrompt) {
            this.setupNameFormControl(extendedState);
            this.updateUIClasses({ mouse: 'move'});
            this._ctx.ui.updateMapClasses();
        }
        return extendedState;

    },

    onStop: function(state) {
        DrawLineString.onStop.call(this, state);

        if (state.name && isnotNull(this._ctx.store.get(state.line.id))) {
            this._ctx.store.setFeatureProperty(state.line.id, 'name', state.name);
        }
        this.removeNameFormControl();
        var y = this._ctx.container.getElementsByClassName('mapbox-ctrl-feature-info');

        var i;
        for (i=0; i < y.length; i++) {y[i].style.display = 'none';};
    },

    onMouseMove: function (state, e) {
        DrawLineString.onMouseMove.call(this, state, e);
        if (state.line.coordinates.length > 1) {
            this.map.fire('drawlinestring.mousemove', {
                feature: state.line,
                state: state
            });
        }
    }, 

    clickAnywhere: function (state, e) {
        if (state.isNameRequired === true && !state.name) {
            return this.changeMode('simple_select');
        } else {
            this.removeNameFormControl();
            return DrawLineString.clickAnywhere.call(this, state, e);
        }
    },
    // onKeyUp: function(state, e) {
    //     if (isEscapeKey(e)) {
    //         this.changeMode('simple_select');
    //       console.log(this._ctx.container.getElementsByClassName('edit-form'));
    //       var y = this._ctx.container.getElementsByClassName('edit-form');
    //       var i;
    //       for (i=0; i < y.length; i++) {y[i].style.display = 'none';};
          
    //     }
    // },

    setupNameFormControl: function (state) {
        this._formContainerEl = document.createElement('div');
        this._formContainerEl.className = 'mapboxgl-draw-named-line--name-container mapboxgl-custom-control';
        this._formContainerEl.id = "LineNameEntryForm";
        this._inputEl = document.createElement('input');
        this._inputEl.type = 'text';
        this._inputEl.className = 'mapboxgl-draw-named-line--name-input';
        if (state.featureName) {
            this._inputEl.value = state.featureName;
        }
        const createButton = document.createElement('button');
        createButton.textContent = 'Create';
        createButton.setAttribute('type', 'button');
        createButton.addEventListener('click', () => this.onCreateButtonClick(state));
        this._inputEl.addEventListener('keyup', (e) => this.onNameInputKeyUp(state, e));
        this._formContainerEl.appendChild(document.createTextNode('Line Name:'));
        this._formContainerEl.appendChild(this._inputEl);
        this._formContainerEl.appendChild(createButton);
        this._msgContainer_el = document.createElement('div');
        this._msgContainer_el.className= 'mapboxgl-draw-named-line--msg-container mapboxgl-custom-control';
        this._msgContainer_el.id = "LineNameMsgForm";
        this._msg_el = document.createElement('p')
        this._msg_el.id = "LineNameMessageTxt"
        this._msgContainer_el.style = 'display: none';
        this._msgContainer_el.appendChild(this._msg_el);
        this._formContainerEl.appendChild(this._msgContainer_el)
        document.body.appendChild(this._formContainerEl);
        this._inputEl.focus();
    },

    removeNameFormControl: function () {
        if (this._formContainerEl && this._formContainerEl.parentNode) {
            this._formContainerEl.parentNode.removeChild(this._formContainerEl);
        }
    },

    startDraw: function() {
        this.updateUIClasses({ mouse: 'add' });
        // Remove by MJN as causes a blank LineString feature to be added to FeatureCollection
        // DrawLineString.onSetup.call(this, {});

        this._ctx.ui.updateMapClasses();
        this.removeNameFormControl();
    },

    onCreateButtonClick: function(state) {
        const name = this._inputEl.value;
        if (name) {
            state.name = name;
            this._msg_el.parentNode.style = 'display: none';
            this.startDraw();
        } else {
            this._msg_el.innerHTML = "The name cannot be blank";
            this._inputEl.focus();
            this._msg_el.parentNode.style = 'display: block';
        }
    },

    onNameInputKeyUp: function(state, e) {
        const name = this._inputEl.value;
        if (name) {
            this._msg_el.parentNode.style = 'display: none';
        };
        if (isEnterKey(e)) {
            if (name) {
                state.name = name;
                this._msg_el.parentNode.style = 'display: none';
                this.startDraw();
            } else {
                this._inputEl.value = 'Line';
                this._msg_el.innerHTML = "The name cannot be blank and has been defaulted to Line";
                this._inputEl.focus();
                this._msg_el.parentNode.style = 'display: block';
            }
            // state.name = name;
            // this.startDraw();
        } else if (isEscapeKey(e)) {
            this.removeNameFormControl();
            // added so you don't need to click 2x on the draw controls to get them working
            DrawLineString.onStop.call(this, state);
        }
    }
})

function isEscapeKey(e) {
    return e.keyCode === 27;
}
  
function isEnterKey(e) {
    return e.keyCode === 13;
}

function isnotNull (object) {
    if (typeof(object) != 'undefined' && object != null)
        { return true}
    else
        {return false};
    }