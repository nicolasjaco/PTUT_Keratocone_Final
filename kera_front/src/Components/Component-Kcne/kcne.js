import React, { useState } from "react";
import { useDropzone } from "react-dropzone";
import sendfiles from "../../Services/service_Kcne";
import DropdownButton from "react-bootstrap/DropdownButton";
import Dropdown from "react-bootstrap/Dropdown";

export default function Dropzone() {
    const { acceptedFiles, getRootProps, getInputProps } = useDropzone();
    const [data, setdata] = useState();
    const [list_type_operation] = useState(["LR", "AIC", "PTK","Aucune"]);
    const [type_op, settypeop]=useState()
  
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
              let response = await sendfiles.get_data(stringBuffer,type_op);
              let responsestr = JSON.stringify(response, null, 4);
              setdata(responsestr);
              console.log({data})
          } catch (error) {
            console.log(error);
          }
        });
      }
    };
  
    const handleSelectedOperation = (e) => {
      const id =e.target.id
      if (id==0){settypeop("LR")}
      if (id==1){settypeop("AIC")}
      if (id==2){settypeop("PTK")}
    };
  
    const type_op_list = Object.entries(list_type_operation);
    const listAllOp = type_op_list.map((list, index) => (
      <Dropdown.Item
        id={index}
        key={index}
        onClick={handleSelectedOperation}
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
              title="Opération"
              className="drop-btn"
            >
              {listAllOp}
          </DropdownButton>
          <div className="div-selected">Type d'opération sélectionné : <div className="methodSelect">{type_op} </div></div>
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