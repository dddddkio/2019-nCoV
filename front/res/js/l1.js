var chartDom_1 = document.getElementById("l1");
var myChart_1 = echarts.init(chartDom_1);
var option_1;

option_1 = {
  tooltip: {
    trigger: "axis",
    position: function (pt) {
      return [pt[0], "70%"];
    },
  },
  xAxis: {
    type: "category",
    data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
  },
  yAxis: {
    type: "value",
    scale: true,
    name: "确诊人数",
    axisLabel: {
      margin: 4,
      formatter: function (value, index) {
        if (value >= 10000 && value < 10000000) {
          value = value / 10000 + "w";
        }
        return value;
      },
    },
  },
  grid: {
    left: 35,
  },
  series: [
    {
      name: "累计确诊人数",
      type: "line",
      symbol: "none",
      itemStyle: {
        color: "rgb(255, 70, 131)",
      },
      data: [150, 230, 224, 218, 135, 147, 260],
    },
  ],
};

option_1 && myChart_1.setOption(option_1, true);

function get_data_l1() {
  $.ajax({
    url: "http://121.5.177.147:8090/api/l1",
    success: function (data) {
      console.log(data);
      option_1.xAxis.data = data.date.reverse();
      option_1.series[0].data = data.confirm.reverse();
      myChart_1.setOption(option_1, true);
      return get_data_l1
    }
  });
}

self.setInterval(get_data_l1(), 10000000);
