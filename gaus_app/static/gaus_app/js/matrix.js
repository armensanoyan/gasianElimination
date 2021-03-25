// location.reload(true);

var xDimValue = document.getElementById('x_dim').value
var yDimValue = document.getElementById('y_dim').value
var xDim = document.getElementById('x_dim')
var yDim = document.getElementById('y_dim')

xDim.addEventListener('change', handleDimantionChange)
yDim.addEventListener('change', handleDimantionChange)

function handleDimantionChange(event) {
    if (event.target.id === 'x_dim') {
        xDimValue = event.target.value
        yDim.value = Number(xDimValue) +1
    } else {
        if (event.target.id === 'y_dim') {
            yDimValue = event.target.value
            xDim.value = Number(yDimValue) - 1
        }
    }
}
// window.history.forward(1);