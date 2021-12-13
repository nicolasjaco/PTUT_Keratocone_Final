import React, { useState } from "react";
import { useDropzone } from "react-dropzone";
import sendfiles from "../../Services/service_Drop";
import DropdownButton from "react-bootstrap/DropdownButton";
import Dropdown from "react-bootstrap/Dropdown";

export default function Kcne() {
  const { acceptedFiles, getRootProps, getInputProps } = useDropzone();
  const [data, setdata] = useState();
  const [listMethode] = useState(["Determiner le KC","Méthode de Stojanovic","Méthode de Mazzotta","Méthode de Wittig-Silva 2008","Méthode de Gomes"]);
  const [methode, setmethode]=useState()

  const files = acceptedFiles.map((file) => (
    <li key={file.path}>{file.path}</li>
  ));

  const __fileReader = (file) => {
    return new Promise((resolve) => {
      var filereader = new FileReader();
      filereader.readAsText(file);  
      filereader.onload = () => {
        resolve(filereader);     
      };
    });
  };

  const sendFiles = async () => {
    for (let file of acceptedFiles) {
      await __fileReader(file).then(async (reader) => {
        try {
            let stringBuffer = reader.result
            let response = await sendfiles.get_data(stringBuffer,methode);
            let responsestr = JSON.stringify(response, null, 4);
            setdata(responsestr);
            console.log({data})
        } catch (error) {
          console.log(error);
        }
      });
    }
  };

  const handleSelectedMethode = (e) => {
    const id =e.target.id
    if (id==0){setmethode("Determiner le KC")}
    if (id==1){setmethode("Méthode de Stojanovic")}
    if (id==2){setmethode("Méthode de Mazzotta")}
    if (id==3){setmethode("Méthode de Wittig-Silva 2008")}
    if (id==4){setmethode("Méthode de Gomes")}
  };

  const methode_list = Object.entries(listMethode);
  const listAllMethode = methode_list.map((list, index) => (
    <Dropdown.Item
      id={index}
      key={index}
      onClick={handleSelectedMethode}
    >
      {list.splice(1)}
    </Dropdown.Item>
  ));

  return (
    <div>
      <section className="box">
        <div className="align" {...getRootProps({ className: "dropzone" })}>
          <input {...getInputProps()} />
          <p className="text">Input your CSV</p>
        </div>
        <aside>
          <ul>{files}</ul>
        </aside>
      </section>
      <div>
        <DropdownButton
            variant="variant"
            title="Methode"
            className="drop-btn"
          >
            {listAllMethode}
        </DropdownButton>
        <div className="div-selected">Méthode sélectionnée : <div className="methodSelect">{methode} </div></div>
      </div>
      <div className="position">
        <button className="btn btn-info" onClick={sendFiles}>
          Envoyer
        </button>
      </div>
      <div className="div-imageid">Result : {data}</div>
    </div>
  );
}