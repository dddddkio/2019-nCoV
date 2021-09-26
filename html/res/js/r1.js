var chartDom_4 = document.getElementById("r1");
var myChart_4 = echarts.init(chartDom_4);
var option_4;

option_4 = {
    series: [{
            data: [{
                name: '累计治愈率',
                value: 55.2
            }],
            type: 'gauge',
            name: '累计治愈率',
            title: {
                show: true,
                offsetCenter: [0, '180%'],
                color: '#fff',
                fontSize: 14
            },
            center: ['25%', '35%'],
            radius: '60%',
            startAngle: '220',
            endAngle: '-40',
            splitNumber: '12',
            pointer: {
                show: true,
                length: '80%'
            },
            itemStyle: {
                normal: {
                    color: {
                        x: '0.00',
                        y: '0.00',
                        x2: '1.00',
                        y2: '1.00',
                        type: 'linear',
                        global: false,
                        colorStops: [{
                                offset: 1,
                                color: '#AF6030'
                            },
                            {
                                offset: 0,
                                color: '#EED25F'
                            }
                        ]
                    }
                }
            },
            axisLine: {
                show: true,
                lineStyle: {
                    width: 8,
                    color: [
                        [
                            1,
                            new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
                                    offset: 0,
                                    color: '#2081DF'
                                },
                                {
                                    offset: 0.5,
                                    color: '#91FCC1'
                                },
                                {
                                    offset: 1,
                                    color: '#2081DF'
                                }
                            ])
                        ]
                    ]
                }
            },
            axisTick: {
                show: false
            },
            splitLine: {
                show: true,
                length: 8,
                lineStyle: {
                    color: '#031544',
                    width: 2
                }
            },
            axisLabel: {
                show: false
            },
            detail: {
                show: true,
                offsetCenter: [0, '110%'],
                color: '#65FDF9',
                fontSize: 28,
                fontWeight: 'bold',
                fontFamily: 'hkxzyW7'
            }
        },
        {
            data: [{
                name: '累计死亡率',
                value: 55.2
            }],
            type: 'gauge',
            name: '累计死亡率',
            title: {
                show: true,
                offsetCenter: [0, '195%'],
                color: '#fff',
                fontSize: 14
            },
            center: ['75%', '40%'],
            radius: '50%',
            startAngle: '220',
            endAngle: '-40',
            splitNumber: '12',
            pointer: {
                show: true,
                length: '80%'
            },
            itemStyle: {
                normal: {
                    color: {
                        x: '0.00',
                        y: '0.00',
                        x2: '1.00',
                        y2: '1.00',
                        type: 'linear',
                        global: false,
                        colorStops: [{
                                offset: 1,
                                color: '#AF6030'
                            },
                            {
                                offset: 0,
                                color: '#EED25F'
                            }
                        ]
                    }
                }
            },
            axisLine: {
                show: true,
                lineStyle: {
                    width: 8,
                    color: [
                        [
                            1,
                            new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
                                    offset: 0,
                                    color: '#2081DF'
                                },
                                {
                                    offset: 0.5,
                                    color: '#91FCC1'
                                },
                                {
                                    offset: 1,
                                    color: '#2081DF'
                                }
                            ])
                        ]
                    ]
                }
            },
            axisTick: {
                show: false
            },
            splitLine: {
                show: true,
                length: 8,
                lineStyle: {
                    color: '#031544',
                    width: 2
                }
            },
            axisLabel: {
                show: false
            },
            detail: {
                show: true,
                offsetCenter: [0, '125%'],
                color: '#B7EBFE',
                fontSize: 20,
                fontFamily: 'hkxzyW7'
            }
        }
    ]
};

function get_data_r1() {
    $.ajax({
      url: "http://121.5.177.147:8090/api/r1",
      success: function (data) {
        option_4.series[0].data[0].value = data.cure_rate;
        option_4.series[1].data[0].value = data.dead_rate;
        myChart_4.setOption(option_4, true);
        return get_data_r1
      },
    });
  }
  
  self.setInterval(get_data_r1(), 10000000);

