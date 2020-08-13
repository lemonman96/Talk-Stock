let canvas = document.getElementById("sentiment_chart");
let ctx = canvas.getContext("2d");
let comp_sent = []
let dates = []
for(let i=0; i<overall_sentiment.length; i++){
    comp_sent.push(overall_sentiment[i].compound)
    dates.push(i);
}
console.log(comp_sent)

let myLineChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: dates,
        datasets:[{
            label: 'test',
            data: comp_sent,
            fill: false,
            borderColor: 'rgb(75, 192, 192)',
            lineTension: 0.1,
        }]
    },
    options: {
        responsive: false
    }
});
