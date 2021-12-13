import React, { useState } from "react";
import Tabs from "react-bootstrap/Tabs";
import Tab from "react-bootstrap/Tab";
import { Fragment } from "react";
import Suivi from "../Components-Suivi/Suivi";
import MyDropzone from "../Components-DropFile/DropFile";
import Kcne from "../Component-Kcne/kcne"

function ControlledTabs() {
  const [key, setKey] = useState(Tabs.Accueil);

  const getCurrentComponent = () => {
    switch (key) {
      case Tabs.Accueil:
        return <MyDropzone/>
      case Tabs.Suivi:
        return <Suivi/>
      case Tabs.KC_Non_Evolutif:
        return <Kcne/>
      case Tabs.KC_Evolutif:
        return <div>Dans KC_Evolutif</div>
    }
  };
  return (
    <Fragment>
      {/* <div className="bg"> */}
      <Tabs
        id="controlled-tab-example"
        activeKey={key}
        onSelect={(k) => setKey(k)}
        className="mb-3 tabs"
      >
        <Tab eventKey={Tabs.Accueil} title="Accueil"></Tab>
        <Tab
          eventKey={Tabs.Suivi}
          title="Suivi Patient"
        ></Tab>
        <Tab eventKey={Tabs.KC_Non_Evolutif} title="Thérapeutique KC NE"></Tab>
        <Tab eventKey={Tabs.KC_Evolutif} title="Thérapeutique KC E"></Tab>
      </Tabs>
      {getCurrentComponent()}
      {/* </div> */}
    </Fragment>
  );
}
Tabs.KC_Evolutif = "Thérapeutique KC E";
Tabs.KC_Non_Evolutif = "Thérapeutique KC NE";
Tabs.Suivi = "Suivi Patient";
Tabs.Accueil="Accueil"

export default ControlledTabs;