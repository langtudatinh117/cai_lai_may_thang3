import React, { Component } from "react";

class LinkCreate extends Component {
    constructor(props) {
        super(props);
        this.state = { error: "" };
    }

    handleSubmit(event) {
        event.preventDefault();
        console.log(this.refs.link.value);
        Meteor.call("links.insert", this.refs.link.value, error => {
            if (error) {
                this.setState({ error: "Enter a valid URL" });
            } else {
                this.setState({ error: "" });
                this.refs.link.value = "";
            }
        });
    }
    render() {
        return (
            <form action="" onSubmit={this.handleSubmit.bind(this)}>
                <div className="form-group">
                    <label htmlFor="">Link to shorten</label>
                    <input ref="link" type="text" className="form-control" />
                </div>
                <div className="text-danger">{this.state.error}</div>
                <button className="btn btn-primary">Shorten!</button>
            </form>
        );
    }
}

export default LinkCreate;
