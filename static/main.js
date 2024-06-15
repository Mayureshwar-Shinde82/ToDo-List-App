document.getElementById('task-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const title = document.getElementById('title').value;
    const description = document.getElementById('description').value;
    const time = document.getElementById('time').value;
    
    const query = `
        mutation {
            createTask(title: "${title}", description: "${description}", time: "${time}", userId: "user_id_placeholder") {
                task {
                    id
                    title
                    description
                    time
                }
            }
        }
    `;
    
    const response = await fetch('/graphql', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + localStorage.getItem('token')
        },
        body: JSON.stringify({ query })
    });
    
    const result = await response.json();
    console.log(result);
});

const loadTasks = async () => {
    const query = `
        query {
            tasks(userId: "user_id_placeholder") {
                id
                title
                description
                time
            }
        }
    `;
    
    const response = await fetch('/graphql', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + localStorage.getItem('token')
        },
        body: JSON.stringify({ query })
    });
    
    const result = await response.json();
    const tasks = result.data.tasks;
    const tasksDiv = document.getElementById('tasks');
    tasksDiv.innerHTML = '';
    tasks.forEach(task => {
        const taskDiv = document.createElement('div');
        taskDiv.innerHTML = `
            <h3>${task.title}</h3>
            <p>${task.description}</p>
            <p>${task.time}</p>
        `;
        tasksDiv.appendChild(taskDiv);
    });
};

loadTasks();
