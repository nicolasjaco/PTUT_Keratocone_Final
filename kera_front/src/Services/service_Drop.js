const sendfiles={
    get_data(csv,methode){
        return fetch('/kera/'+ methode, {
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