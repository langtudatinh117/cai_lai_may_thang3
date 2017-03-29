var util = require("util"),
    http = require("http");

var options = {
    host: "http://www.oxfordlearnersdictionaries.com/definition/english/crucial",
    path: "/"
};

var content = "";   

var req = http.request(options, function(res) {
    res.setEncoding("utf8");
    res.on("data", function (chunk) {
        content += chunk;
    });

    res.on("end", function () {
        util.log(content);
    });
});

req.end();