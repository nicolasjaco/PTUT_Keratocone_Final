const sendfiles={
    get_data(csv,type_op){
        return fetch('/kcne/'+type_op, {
            credentials: 'include',
            method: 'POST',
            headers: {
              Accept: 'application/vnd.ms-excel',
              'Content-Type': 'application/vnd.ms-excel'
            }
            ,
            body: csv
          }).then( (answer) => {
            return (answer.json())
          }).catch((error) => { throw error })
        },
  }
  export default  sendfiles