// get parent container div from which the script is called
const parent = document.currentScript.parentElement

// define list of spots
const spot_list = [1, 9, 11, 15, 17, 21, 22, 30, 31, 32, 36, 39, 43, 44, 47,
    51, 53, 54, 63, 66, 68, 79, 89, 92, 94, 103]

// for each spot, show a list item with the text "Spot #" where # is the spot number
// and with a hyperlink to the spot's page, which is the "spot#.html" file in the "spots" folder
spot_list.forEach(function (spot) {
    const li = document.createElement('li')
    const a = document.createElement('a')
    a.href = `spots/spot${spot}.html`
    a.innerText = `Spot ${spot}`
    li.appendChild(a)
    parent.appendChild(li)
})
