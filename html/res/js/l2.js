var chartDom_2 = document.getElementById('l2');
var myChart_2 = echarts.init(chartDom_2);
var option_2;
var date
option_2 = {
    // xAxis: {
    //     type: 'category',
    //     data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    // },
    // yAxis: {
    //     type: 'value',
    //     name:"确诊人数",
    // },
    // series: [{
    //     data: [250, 230, 224, 218, 135, 147, 260],
    //     type: 'line'
    // }]
    tooltip: {
        trigger: 'axis',
        position: function (pt) {
            return [pt[0], '70%'];
        }
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: date
    },
    yAxis: {
        type: 'value',
        boundaryGap: [0, '100%']
    },
    series: [
        {
            name: '新增确诊人数',
            type: 'line',
            symbol: 'none',
            sampling: 'lttb',
            itemStyle: {
                color: 'rgb(255, 70, 131)'
            },
            areaStyle: {
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: 'rgb(255, 158, 68)'
                }, {
                    offset: 1,
                    color: 'rgb(255, 70, 131)'
                }])
            },
            data: []
        }
    ]
};

option_2 && myChart_2.setOption(option_2,true);

function get_data_l2(){
    $.ajax({
        url: "http://121.5.177.147:8090/api/l2",
        success: function(data){
            console.log(data);
            option_2.xAxis.data = data.date.reverse()
            option_2.series[0].data = data.confirm_add.reverse()
            myChart_2.setOption(option_2,true)
            return get_data_l2
        }
    })
}


self.setInterval(get_data_l2(),10000000);
