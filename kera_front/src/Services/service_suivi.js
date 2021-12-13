const suivi = {
    post_suivi(age, consultation, KC) {
      return fetch(
        "/suivi/"+age+"/"+consultation+"/"+KC,
        {
          method: "POST",
          headers: {
            Accept: "application/text",
            "Content-Type":  "charset=utf-8",
          },
          body:age,consultation,KC
          
        }
      )
        .then((answer) => {
          return answer.json();
        })
        .catch((error) => {
          throw error;
        });
    }
}
export default  suivi