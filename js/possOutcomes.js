function getInputs(){
    var tb = document.querySelector('input[name="topBottom"]:checked').value;
    var inning = document.getElementById("inning").value
    var totalInning = tb + "" + inning;
    var outs = document.querySelector('input[name="outs"]:checked').value;
    var first = document.getElementById("first").checked ? 1 : 0
    var second = document.getElementById("second").checked ? 1 : 0
    var third = document.getElementById("third").checked ? 1 : 0
    var scoreDiff = gameScoreDiff
    var strikes = document.querySelector('input[name="strikes"]:checked').value;
    var balls = document.querySelector('input[name="balls"]:checked').value;

    return {
        inning:totalInning,
        outs:outs,
        first:first,
        second:second,
        third:third,
        scoreDiff:scoreDiff,
        strikes:strikes,
        balls:balls
    }
}

function givenOrDefault(given, def, type) {
    if (typeof given[type] !== 'undefined') {
        return given[type];
    } else {
        return def[type];
    }
}
function getResults(inputDict,changes) {
    const inpInning = givenOrDefault(changes,inputDict,'inning');
    const inpScoreDiff = givenOrDefault(changes,inputDict,'scoreDiff');
    const inpOuts = givenOrDefault(changes,inputDict,'outs');
    const inpBalls = givenOrDefault(changes,inputDict,'balls');
    const inpStrikes = givenOrDefault(changes,inputDict,'strikes');
    const inpFirst = givenOrDefault(changes,inputDict,'first');
    const inpSecond = givenOrDefault(changes,inputDict,'second');
    const inpThird = givenOrDefault(changes,inputDict,'third');
    return JSON[inpInning][inpScoreDiff][inpOuts][inpBalls][inpStrikes][inpFirst][inpSecond][inpThird];
}

function appendToOutcomeList(item){
    const outcomeList = document.getElementById('outcomeList');
    var node = document.createElement("LI");
    var textnode = document.createTextNode(item);
    node.appendChild(textnode);
    outcomeList.appendChild(node);
}

function seePossOutcomes(inputDict){
    document.getElementById('outcomeList').innerHTML = "";
    const ballOutcome = ball(inputDict);
    if(ballOutcome){
        appendToOutcomeList("Ball: " + getProbability(ballOutcome));
    }
    const walkOutcome = walk(inputDict);
    if(walkOutcome){
        appendToOutcomeList("Walk: " + getProbability(walkOutcome));
    }
    const strikeOutcome = strike(inputDict);
    if(strikeOutcome){
        appendToOutcomeList("Strike: " + getProbability(strikeOutcome));
    }
    const strikeoutOutcome = strikeOut(inputDict);
    if(strikeoutOutcome){
        appendToOutcomeList("Strikeout: " + getProbability(strikeoutOutcome));
    }
    const homerunOutcome = homerun(inputDict);
    if(homerunOutcome){
        appendToOutcomeList("Homerun: " + getProbability(homerunOutcome));
    }
}

function getProbability(outcome){
    return (outcome['1'] / (outcome['0'] + outcome['1']) * 100).toFixed(2) + "%";
}

//outcome functions
function ball(inputDict){
    let balls = parseInt(inputDict.balls);
    if(balls == 3){
        return;
    }
    balls++;
    const changes = {
        balls :balls
    }
    return getResults(inputDict, changes);
}

function strike(inputDict){
    let strikes = parseInt(inputDict.strikes);
    if(strikes == 2){
        return;
    }
    strikes++;
    const changes = {
        strikes :strikes
    }
    return getResults(inputDict, changes);
}

function walk(inputDict){
    if(inputDict.balls != 3){
        return;
    }
    let first = inputDict.first;
    let second = inputDict.second;
    let third = inputDict.third;
    let scoreDiff = inputDict.scoreDiff;
    if(first == 1){
        if(second == 1){
            if(third == 1){
                if(inputDict.inning.charAt(0) == '0'){
                    scoreDiff --;
                }
                else{
                    scoreDiff ++;
                }
            }
            third = 1;
        }
        second = 1;
    }
    first = 1;
    const changes = {
        balls: 0,
        strikes: 0,
        first: first,
        second:second,
        third: third,
        scoreDiff: scoreDiff
    }
    return getResults(inputDict,changes);
}

function strikeOut(inputDict){
    let changes = {}
    if(inputDict.strikes != 2){
        return;
    }
    if(inputDict.outs == 2){
        let inning = inputDict.inning;
        if (inning.charAt(0) == 0 ){
            //top
            inning = '1' + inning.substring(1);
        }
        else{
            let curInning = inning.substring(1);
            if(curInning == '9+' || curInning == '9'){
                inning = '09+';
            }
            else{
                inning = '0' + (parseInt(curInning) + 1);
            }
        }
        changes = {
            inning: inning,
            strikes:0,
            balls:0,
            first:0,
            second:0,
            third:0,
            outs:0
        }
        return getResults(inputDict,changes);
    }
    else{
        changes = {
            strikes:0,
            balls:0,
            outs: (parseInt(inputDict.outs) + 1)
        }
    }
    return getResults(inputDict,changes);
}
function homerun(inputDict){
    const runs = parseInt(inputDict.first) + parseInt(inputDict.second) + parseInt(inputDict.third) + 1;
    let scoreDiff = inputDict.scoreDiff;
    if(inputDict.inning.charAt(0) == '0'){
        scoreDiff -= runs;
    }
    else{
        scoreDiff += runs;
    }
    const changes = {
        scoreDiff: scoreDiff,
        first: 0,
        second: 0,
        third: 0,
        balls: 0,
        strikes: 0
    }
    return getResults(inputDict,changes);
}