const quiz = [
    {
        'ques': "Q1",
        'a': "a1",
        'b': "b1",
        'c': "c1",
        'd': "d1",
        "correct": 'a'
    },
    {
        'ques': "Q2",
        'a': "a2",
        'b': "b2",
        'c': "c2",
        'd': "d2",
        "correct": 'a'
    },
    {
        'ques': "Q3",
        'a': "a3",
        'b': "b3",
        'c': "c3",
        'd': "d3",
        "correct": 'a'
    },
    {
        'ques': "Q4",
        'a': "a4",
        'b': "b4",
        'c': "c4",
        'd': "d4",
        "correct": 'a'
    },
      
];

const quizEl = document.getElementById("quiz");
const answerEls = document.querySelectorAll(".answer");
const quesEl = document.getElementById("ques");
const aEl = document.getElementById("a_text");
const bEl = document.getElementById("b_text");
const cEl = document.getElementById("c_text");
const dEl = document.getElementById("d_text");

let cnt = 0;
let score = 0;
function getQues() {
    clearSel();
    const currData = quiz[cnt];
    quesEl.innerText = currData.ques;
    aEl.innerText = currData.a;
    bEl.innerText = currData.b;
    cEl.innerText = currData.c;
    dEl.innerText = currData.d;
};

function clearSel() {
    answerEls.forEach((answerEl) => {
        answerEl.checked = false;
    });
}

function checkAns() {
    let ans = undefined;
    answerEls.forEach((answerEl) => {
        if(answerEl.checked)
            ans = answerEl.id;
    });

    return ans;
}

getQues();
const btEl = document.getElementById('submit');
btEl.addEventListener('click', () => {
    let ans = checkAns();
    if(!ans)
        return;
    if(ans === quiz[cnt].correct)
        score++;

    cnt++;
    // console.log(score);
    if(cnt >= quiz.length) {
        quizEl.innerHTML = `
        <h2>Score: ${score}/${quiz.length}</h2>
        <button onclick=location.reload()>Restart</button>
        `;
    }
    else
        getQues();
});
