'use strict';

function Welcome(props) {
    return <h2 className='welcome'>I have a number in my mind. Can you guess?</h2>;
}

function Starter(props) {
    return <button className='starter'>Start</button>;
}

function GuessInput(props) {
    return <input />
}

function App(props) {
    return (
        <div className='base-container'>
        <div className='head-container'>
            <Starter />
            <Welcome />
        </div>
        <div className='body-container'>
            <GuessInput />
        </div>
        </div>
    );
}

ReactDOM.render(
    <App />,
    document.getElementById('root')
);

