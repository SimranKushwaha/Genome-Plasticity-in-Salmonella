// get parent container div from which the script is called
const parent = document.currentScript.parentElement

// define list of spots
const spot_list = [1, 9, 11, 15, 17, 21, 22, 30, 31, 32, 36, 39, 43, 44, 47,
    51, 53, 54, 63, 66, 68, 79, 89, 92, 94, 103]

// for each spot, show a list item with the text "Spot #" where # is the spot number
// and with a hyperlink to the spot's page, which is the "spot#.html" file in the "spots" folder
// Each hyperlink is quite small. We can show four hyperlinks per row.
// The parent container div is used to show the list.
const table = document.createElement('table');
const tbody = document.createElement('tbody');
let row, cell, link, spotNum;

for (let i = 0; i < spot_list.length; i++) {
    if (i % 4 === 0) {
        row = document.createElement('tr');
        tbody.appendChild(row);
    }

    cell = document.createElement('td');
    link = document.createElement('a');
    spotNum = spot_list[i];

    link.setAttribute('href', `spots/spot${spotNum}.html`);
    link.textContent = `Spot ${spotNum}`;

    cell.appendChild(link);
    row.appendChild(cell);
}

table.appendChild(tbody);
table.style.borderCollapse = 'collapse';
table.style.border = 'none';
parent.appendChild(table);
