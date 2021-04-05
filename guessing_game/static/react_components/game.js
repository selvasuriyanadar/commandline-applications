'use strict';

function Welcome(props) {
    return React.createElement(
        'h2',
        { className: 'welcome' },
        'I have a number in my mind. Can you guess?'
    );
}

function Starter(props) {
    return React.createElement(
        'button',
        { className: 'starter' },
        'Start'
    );
}

function GuessInput(props) {
    return React.createElement('input', null);
}

function App(props) {
    return React.createElement(
        'div',
        { className: 'base-container' },
        React.createElement(
            'div',
            { className: 'head-container' },
            React.createElement(Starter, null),
            React.createElement(Welcome, null)
        ),
        React.createElement(
            'div',
            { className: 'body-container' },
            React.createElement(GuessInput, null)
        )
    );
}

ReactDOM.render(React.createElement(App, null), document.getElementById('root'));