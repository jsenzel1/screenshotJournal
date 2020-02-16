let masterIndex;
let dates = [];

function setup() {
  masterIndex = loadStrings("/int.txt", loadTxt);
  // masterIndex = loadStrings("/int.txt", loadTxt);
  noCanvas();

}

function loadTxt(incomingString) {
  print(incomingString);

  dates = loadStrings('dates.txt', mySetup)

}



function mySetup() {


  print(masterIndex[0]);

  print(dates);

  for (let i = 0; i < masterIndex; i++) {
    let imgString = "/caps/" + i + ".jpg";
    createImg(imgString);

    let dateString = dates[i];

    createP(dateString);

  }


}

function draw() {
  print((txts[1])[0]);
  print('draw');
  background(220);
}