import React, { useState, useEffect } from "react";
import DropdownButton from "react-bootstrap/DropdownButton";
import Dropdown from "react-bootstrap/Dropdown";
import { Button } from "react-bootstrap";
import suivi from "../../Services/service_suivi"

function Suivi() {

  const [listAge, setlistAge] = useState(["moins de 15","15 a 20","20 a 30","30 a 40","plus de 40"]);
  const [age, setAge]=useState()
  const [listConsultation, setlistConsultation] = useState(["oui","non"]);
  const [consu, setConsu]=useState()
  const [listKC, setlistKC] = useState(["léger","modéré","sévère"]);
  const [KC, setKC]=useState()
  const [suiviAnswer,setSuiviAnswer]=useState("Résultat");

  const handleSelectedAge = (e) => {
    const id =e.target.id
    if (id==0){setAge("moins de 15")}
    if (id==1){setAge("15 a 20")}
    if (id==2){setAge("20 a 30")}
    if (id==3){setAge("30 a 40")}
    if (id==4){setAge("plus de 40")}
  };

  const handleSelectedConsultation = (e) => {
    const id =e.target.id
    if (id==0){setConsu("oui")}
    if (id==1){setConsu("non")}
  };

  const handleSelectedKC = (e) => {
    const id =e.target.id
    if (id==0){setKC("léger")}
    if (id==1){setKC("modéré")}
    if (id==2){setKC("sévère")}
  };

  const handleSuivi = async () => {
    let answer;
    try {
      answer = await suivi.post_suivi(
        age,
        consu,
        KC
      );
      setSuiviAnswer(answer);
    } catch (error) {
      console.log(error)
    }
  };

  const age_list = Object.entries(listAge);
  const listAllAge = age_list.map((list, index) => (
    <Dropdown.Item
      id={index}
      key={index}
      onClick={handleSelectedAge}
    >
      {list.splice(1)}
    </Dropdown.Item>
  ));

  const consu_list = Object.entries(listConsultation);
  const listAllConsu = consu_list.map((list, index) => (
    <Dropdown.Item
      id={index}
      key={index}
      onClick={handleSelectedConsultation}
    >
      {list.splice(1)}
    </Dropdown.Item>
  ));

  const kc_list = Object.entries(listKC);
  const listAllKC = kc_list.map((list, index) => (
    <Dropdown.Item
      id={index}
      key={index}
      onClick={handleSelectedKC}
    >
      {list.splice(1)}
    </Dropdown.Item>
  ));

  return (
    <div>
          <DropdownButton
            variant="info"
            title="Age"
            className="drop-btn"
          >
            {listAllAge}
          </DropdownButton>
      <div className="div-selected">Age du patient : {age} </div>

          <DropdownButton
            variant="warning"
            title="Consultation"
            className="drop-btn"
          >
            {listAllConsu}
          </DropdownButton>
      <div className="div-selected">Est-ce la première consultation ? : {consu} </div>

      <DropdownButton
            variant="info"
            title="KC"
            className="drop-btn"
          >
            {listAllKC}
          </DropdownButton>
      <div className="div-selected">Quel est l'état du KC ? : {KC} </div>
      <div className="btn-valider">
      <Button
          className="btn btn-warning btn-valider"
          onClick={handleSuivi}
        >
          Valider
        </Button>
        </div>
        <div className="frame-strSuivi">
        {JSON.stringify(suiviAnswer, null, 4)}
      </div>
    </div>
    
  )
}

export default Suivi;
