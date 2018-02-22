import Vue  from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        usercount:{
            realtime: 1111,
            total: 2222,
            portal_today: 3333,
            portal_total: 444
        },
        recent_users: [
            {title: '--'},
            {title: '--'},
            {title: '--'},
            {title: '--'},
            {title: '--'}
        ],
        environment: {
            temp: '16',
            humidity: '36',
            moisture: '16',
            winds: '16'
        }
    },
    mutations: {
        PUSH_RECENT_USERS(state, user) {
            // 加一个删一个
            state.recent_users.pop();
            state.recent_users.unshift(user);
        },
        SET_USER_COUNT(state, usercount) {
            // console.log(usercount)
            state.usercount = usercount
        },
        UPDATE_ENVIRONMENT(state, data) {
            state.environment = data
        }
    },
    actions: {
        pushRecentUser({commit}, log) {
            commit('PUSH_RECENT_USERS', log);
        },
        setUserCount({commit}, log) {
            commit('SET_USER_COUNT', log);
        },
        updateEnvironment({commit}, data) {
            commit('UPDATE_ENVIRONMENT', data);
        },
    },
    getters: {
        getLogs: (state) => state.logs
    }
})