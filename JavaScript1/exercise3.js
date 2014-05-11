function returnDuplicates(list) {
    var returnList = [];
    // create a copy of list so that list remains the same. 
    var dupList = [];
    for (var index = 0; index < list.length; index++) {
        dupList.push(list[index])
    } // end for loop that create dupList
    for (var index1 = 0; index1 < dupList.length -1; index1++) {
        var count = 1;
        for (var index2 = index1 + 1; index2 < dupList.length; index2++) {
                if (dupList[index1] === dupList[index2]) {
                    count++;
                    delete dupList[index2];
                } // end of equality if statement
        } // end of second for loop
        if (count > 1) {
            if (typeof dupList[index1] !== 'undefined'){
                returnList.push(dupList[index1]);
            } // end of if statement
        } // end of count if statement
    } // end of first for loop
    return returnList;
} // end of returnDuplicates function


var x = ['panther', 'frog', 'panther', 'cat', 2, 3, 2, 1];
var classroomIds = [47, 12, 19, 22, 26, 99, 30, 50, 324, 003, 44, 33, 346, 354, 44, 235, 45, 34, 44, 590, 09, 099, 0, 1, 3, 33, 999, 9];
var randomJunkIFound = ["katie", "true", true, 19, "gargoyles", "!", 2 + 3, "2 + 3", 19, "19", 19 === "19", 6, false, false];
var hackbrightStudents = ["katie", "amy", "jenny", "katie", "kelley", "katie", "amy"]
console.log(returnDuplicates(hackbrightStudents));


// dict.key returns value only, didn't work above in if stmt because not set yet
// dict[key] can set value