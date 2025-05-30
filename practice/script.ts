function simulate(entries: number[], s: number): number[] {
  // Write the code that goes here
  const unaffected_items = entries.slice(s,-s)
  const ones = new Array()
  for (let i = 0; i < s; i++) {
        ones.push(-1)
    }
  const adapted_entries: number[] = [...ones, ...unaffected_items, ...ones]
  return adapted_entries;
}

let records: number[] = [ 4, 1, 3, 5, 4, 7, 9 ];
console.log(simulate(records, 3));

records = [ 7, 6, 9, 1, 8, 3, 2 ];
console.log(simulate(records, 2));