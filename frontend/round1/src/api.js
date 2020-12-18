import axios from 'axios'
const instance = axios.create({
    baseURL: 'http://localhost:5000',
    headers: {
        'content-type':'application/json',
    }
});
export default {
    getWeeklyCommitsList: (symbol) =>
    instance({
        'method':'GET',
        'url':'/commits/weekly',
    }),
    getMonthlyCommitsList: (symbol) =>
    instance({
        'method':'GET',
        'url':'/commits/monthly',
    }),
    getCommittersList: (symbol) =>
    instance({
        'method':'GET',
        'url':'/committers',
    }),
    getLangaguesList: (symbol) =>
    instance({
        'method':'GET',
        'url':'/languages',
    })
}