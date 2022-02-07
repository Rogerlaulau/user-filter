const result = document.getElementById('result')
const filter = document.getElementById('filter')
const listItems = []

getData()

filter.addEventListener('input', (e) => filterData(e.target.value))

async function getData() {
    // const res = await fetch('https://randomuser.me/api?results=50')
    const res = await fetch('http://localhost:5001/participant')

    const { results } = await res.json()

    // Clear result
    result.innerHTML = ''

    results.forEach(user => {
        const li = document.createElement('li')

        listItems.push(li)

        li.innerHTML = `
            <img src="${user.icon}" alt="${user.name.first}">
            <div class="user-info">
                <h4>${user.name.first} ${user.name.last}</h4>
                <p>${user.item}</p>
            </div>
        `

        result.appendChild(li)
    })
}

function filterData(searchTerm) {
    listItems.forEach(item => {
        if(item.innerText.toLowerCase().includes(searchTerm.toLowerCase())) {
            item.classList.remove('hide')
        } else {
            item.classList.add('hide')
        }
    })
}