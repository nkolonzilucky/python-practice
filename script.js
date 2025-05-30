var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
function simulate(entries, s) {
    // Write the code that goes here
    //   console.log(entries.slice(0,s))
    //   console.log(entries.slice(-s))
    var unaffected_items = entries.slice(s, -s);
    var ones = new Array();
    for (var i = 0; i < s; i++) {
        ones.push(-1);
    }
    var adapted_entries = __spreadArray(__spreadArray(__spreadArray([], ones, true), unaffected_items, true), ones, true);
    console.log(adapted_entries.slice(s, -s));
    return adapted_entries;
}
var records = [4, 1, 3, 5, 4, 7, 9];
console.log(simulate(records, 3));
records = [7, 6, 9, 1, 8, 3, 2];
console.log(simulate(records, 2));
