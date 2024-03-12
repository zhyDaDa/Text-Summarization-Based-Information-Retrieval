const btn = document.querySelector("#mainSearchBTN");
const formElement = document.querySelector("#mainSearchForm");
const smartSearch = document.querySelector("#smartSearch");

// btn.addEventListener("click", (e) => {
//     e.preventDefault();
//     const data = new FormData(formElement);
//     let gender = data.get('gender'); // 男 女 全部
//     let ageMin = data.get('ageMin');
//     let ageMax = data.get('ageMax');
//     let bodyPart = data.get('bodyPart');
//     let symptom = data.get('symptom');
//     let illness = data.get('illness');

//     let postData = JSON.stringify({
//         gender: gender,
//         ageMin: ageMin,
//         ageMax: ageMax,
//         bodyPart: bodyPart,
//         symptom: symptom,
//         illness: illness
//     });

//     // post请求
//     fetch("/select/", {
//         method: "POST",
//         body: postData,
//     });

// });