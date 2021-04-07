'use strict';

function Welcome(props) {
    return React.createElement('h2', { className: 'welcome' }, 'Toss Me!!');
}

function MenuButton(props) {
    return React.createElement('button', { className: 'menu-button' }, props.text);
}

function TossInput(props) {
    return React.createElement('button', { className: 'hitter' });
}

function Head(props) {
    return React.createElement('div', { className: 'head-container' }, React.createElement(MenuButton, { text: 'Start' }), React.createElement(Welcome, null), React.createElement(MenuButton, { text: 'Help' }));
}

function Body(props) {
    return React.createElement('div', { className: 'body-container' }, React.createElement(TossInput, null));
}

function App(props) {
    return React.createElement('div', { className: 'base-container' }, React.createElement(Head, null), React.createElement(Body, null));
}

ReactDOM.render(React.createElement(App, null), document.getElementById('root'));
