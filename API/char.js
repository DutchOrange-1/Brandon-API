// import Chart from '/chart.umd.js'
let amout = 50;

window.onload = async function () {
    const topInput = document.getElementById('topInput');
    topInput.addEventListener('change', function () {
        amout = topInput.value;
        console.log('Input changed to:', amout);
        update_graph();
    });

    update_graph();
}


async function fetchData(id) {
    const url = 'http://api.brandon.net.za/temp_collect?name=brandon&token=LDvvblTbOQNlgMKXcnGPnphRYGyyZf&probe_id=' + id + '&amount=' + amout;

    try {
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error(`Failed to fetch data. Status: ${response.status}`);
        }

        const data = await response.json();
        // console.log(data);
        // data[1];

        // Format data for Chart.js
        const chartData = Object.entries(data[1]).map(([timestamp, value]) => ({
            x: timestamp,
            y: parseFloat(value)
        }));

        // console.log("NEW DATA: ", chartData);

        const chartData_updated = chartData.map(({ x, y }) => {
            const dateObject = new Date(x);
            const formattedDate = `${dateObject.getMonth() + 1}/${dateObject.getDate().toString().padStart(2, '0')} ${dateObject.getHours().toString().padStart(2, '0')}:${dateObject.getMinutes().toString().padStart(2, '0')}:${dateObject.getSeconds().toString().padStart(2, '0')}`;
            return {
                x: dateObject,
                y: y,
                formattedDate: formattedDate
            };
        });

        // console.log("UPDATED: ", chartData_updated)
        return chartData_updated;

    } catch (error) {
        console.error('Error fetching data:', error.message);
    }
}


async function update_graph() {

    // Get JSON
    const data1 = await fetchData(1);
    const data2 = await fetchData(2);
    console.log("DATA1: ", data1);
    console.log("DATA2: ", data2);




    var chart = new CanvasJS.Chart("chartContainer", {
        animationEnabled: true,
        title: {
            text: "Temperature"
        },
        axisX: {
            title: "Time",
            type: 'time',
            time: {
                unit: 'day', // Set the unit to 'day'
                displayFormats: {
                    day: 'MMM D' // Customize the display format for day of the month
                }
            }
        },
        axisY: {
            title: "Green Probe",
            suffix: "Cº",
            includeZero: true
        },
        data: [{
            type: "line",
            name: "Temperature1",
            connectNullData: true,
            xValueType: "dateTime",
            dataPoints: data1
        },
        {
            type: "line",
            name: "Temperature2",
            connectNullData: true,
            xValueType: "dateTime",
            dataPoints: data2
        }
        ]
    });

    console.log("Chart Renderd");
    chart.render();
}

