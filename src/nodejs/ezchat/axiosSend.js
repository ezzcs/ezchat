module.paths.push("/usr/local/lib/node_modules");

const axios = require('axios');

const data = {
    searchID: '1',
    res_list: 'Content Writer'
};

axios.post('http://192.168.44.7:8886', data)
    .then((res) => {
        console.log(`Status: ${res.status}`);
        console.log('Body: ', res.data);
    }).catch((err) => {
        console.error(err);
    });

