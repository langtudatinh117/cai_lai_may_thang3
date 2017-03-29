import React, { Component } from "react";
import Header from "./header";
import BinList from "./bins/bins_list";

class app extends Component {
    render() {
        return <div><Header /><BinList /></div>;
    }
}

export default app;
