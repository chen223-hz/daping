import store from '../store'

export default {
	install(Vue, url) {
		let socket;
        socket = new WebSocket(url);
		//Vue.prototype.$socket = socket;
		Vue.prototype.$socket = this;

        socket.onmessage = function (event) {
            var data = JSON.parse(event.data)
            /* 
            if (data.action == 'pushRecentUser') {
                store.dispatch('pushRecentUser', data.data);
            }
            if (data.action == 'setUserCount') {
                store.dispatch('setUserCount', data.data);
            }
            if (data.action == 'updateEnvironment') {
                store.dispatch('setUserCount', data.data);
            }
            */
            // 当第三次遇到基本类似的代码，我们就要想想怎么简化它了
            // 我们可以要求数据算好了再进接口，这是简化项目整体复杂度该做的事
            // 尽管只写store.dispatch一行也行，但是我们还是要加一些数据的验证，以防止一些灵异的问题
            const actions = ['pushRecentUser', 'setUserCount', 'updateEnvironment']
            if (actions.indexOf(data.action) > -1) {
                store.dispatch(data.action, data.data)
            }
            //console.log(data);
        }
        socket.onopen = function (event) {
            var message = {
                action: 'echo',
                data: 'on'
            };
            socket.send(JSON.stringify(message));
        }
        this.send = function (message, callback) {
            this.waitForConnection(function () {
                socket.send(message);
                if (typeof callback !== 'undefined') {
                    callback();
                }
            }, 1000);
        };
        this.waitForConnection = function (callback, interval) {
            if (socket.readyState === 1) {
                callback();
            } else {
                var that = this;
                // optional: implement backoff for interval here
                setTimeout(function () {
                    that.waitForConnection(callback, interval);
                }, interval);
            }
        };
    }
}