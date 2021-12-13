import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import ControlledTabs from "./Components/Component-Tabs/Tabs";
import "bootstrap/dist/css/bootstrap.min.css";

class App extends React.Component {
  render() {
    return (
      <div>
        <div className="d-flex justify-content-center title image-title">
          {/* <Image src={image} fluid height="25%" width="25%" /> */}
          <div>
            <h1 className="titre-h1">Systeme expert</h1>
          </div>
        </div>
          <ControlledTabs />
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("root"));
