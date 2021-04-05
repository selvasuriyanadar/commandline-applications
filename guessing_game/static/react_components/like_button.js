'use strict';

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var LikeButton = function (_React$Component) {
    _inherits(LikeButton, _React$Component);

    function LikeButton(props) {
        _classCallCheck(this, LikeButton);

        var _this = _possibleConstructorReturn(this, (LikeButton.__proto__ || Object.getPrototypeOf(LikeButton)).call(this, props));

        _this.state = { liked: false };
        return _this;
    }

    _createClass(LikeButton, [{
        key: 'render',
        value: function render() {
            var _this2 = this;

            if (this.state.liked) {
                return 'You liked this.';
            }

            return React.createElement(
                'button',
                { onClick: function onClick() {
                        return _this2.setState({ liked: true });
                    } },
                'Like'
            );
        }
    }]);

    return LikeButton;
}(React.Component);

var Clock = function (_React$Component2) {
    _inherits(Clock, _React$Component2);

    function Clock(props) {
        _classCallCheck(this, Clock);

        var _this3 = _possibleConstructorReturn(this, (Clock.__proto__ || Object.getPrototypeOf(Clock)).call(this, props));

        _this3.state = { date: new Date() };
        return _this3;
    }

    _createClass(Clock, [{
        key: 'componentDidMount',
        value: function componentDidMount() {
            var _this4 = this;

            this.timerID = setInterval(function () {
                return _this4.tick();
            }, 1000);
        }
    }, {
        key: 'componentWillUnmount',
        value: function componentWillUnmount() {
            clearInterval(this.timerID);
        }
    }, {
        key: 'tick',
        value: function tick() {
            this.setState({
                date: new Date()
            });
        }
    }, {
        key: 'render',
        value: function render() {
            return React.createElement(
                'div',
                null,
                React.createElement(
                    'h1',
                    null,
                    'Hello, world!'
                ),
                React.createElement(
                    'h2',
                    null,
                    'It is ',
                    this.state.date.toLocaleTimeString(),
                    '.'
                )
            );
        }
    }]);

    return Clock;
}(React.Component);

var Toggle = function (_React$Component3) {
    _inherits(Toggle, _React$Component3);

    function Toggle(props) {
        _classCallCheck(this, Toggle);

        var _this5 = _possibleConstructorReturn(this, (Toggle.__proto__ || Object.getPrototypeOf(Toggle)).call(this, props));

        _this5.state = { isToggleOn: true };

        // This binding is necessary to make `this` work in the callback
        _this5.handleClick = _this5.handleClick.bind(_this5);
        return _this5;
    }

    _createClass(Toggle, [{
        key: 'handleClick',
        value: function handleClick() {
            this.setState(function (state) {
                return {
                    isToggleOn: !state.isToggleOn
                };
            });
        }
    }, {
        key: 'render',
        value: function render() {
            return React.createElement(
                'button',
                { onClick: this.handleClick },
                this.state.isToggleOn ? 'ON' : 'OFF'
            );
        }
    }]);

    return Toggle;
}(React.Component);

function UserGreeting(props) {
    return React.createElement(
        'h1',
        null,
        'Welcome back!'
    );
}

function GuestGreeting(props) {
    return React.createElement(
        'h1',
        null,
        'Please sign up.'
    );
}

function Greeting(props) {
    var isLoggedIn = props.isLoggedIn;
    if (isLoggedIn) {
        return React.createElement(UserGreeting, null);
    }
    return React.createElement(GuestGreeting, null);
}

function LoginButton(props) {
    return React.createElement(
        'button',
        { onClick: props.onClick },
        'Login'
    );
}

function LogoutButton(props) {
    return React.createElement(
        'button',
        { onClick: props.onClick },
        'Logout'
    );
}

var LoginControl = function (_React$Component4) {
    _inherits(LoginControl, _React$Component4);

    function LoginControl(props) {
        _classCallCheck(this, LoginControl);

        var _this6 = _possibleConstructorReturn(this, (LoginControl.__proto__ || Object.getPrototypeOf(LoginControl)).call(this, props));

        _this6.handleLoginClick = _this6.handleLoginClick.bind(_this6);
        _this6.handleLogoutClick = _this6.handleLogoutClick.bind(_this6);
        _this6.state = { isLoggedIn: false };
        return _this6;
    }

    _createClass(LoginControl, [{
        key: 'handleLoginClick',
        value: function handleLoginClick() {
            this.setState({ isLoggedIn: true });
        }
    }, {
        key: 'handleLogoutClick',
        value: function handleLogoutClick() {
            this.setState({ isLoggedIn: false });
        }
    }, {
        key: 'render',
        value: function render() {
            var isLoggedIn = this.state.isLoggedIn;
            var button = void 0;
            if (isLoggedIn) {
                button = React.createElement(LogoutButton, { onClick: this.handleLogoutClick });
            } else {
                button = React.createElement(LoginButton, { onClick: this.handleLoginClick });
            }

            return React.createElement(
                'div',
                null,
                React.createElement(Greeting, { isLoggedIn: isLoggedIn }),
                button
            );
        }
    }]);

    return LoginControl;
}(React.Component);

function App(props) {
    return React.createElement(
        'div',
        null,
        React.createElement(LoginControl, null),
        React.createElement(
            'div',
            null,
            React.createElement(Clock, null),
            React.createElement(Toggle, null),
            React.createElement(LikeButton, null)
        )
    );
}

ReactDOM.render(React.createElement(App, null), document.getElementById('root'));