var app = new Vue({
  el: "#app",
  data: {
    confirm: 0,
    suspect: 0,
    heal: 0,
    dead: 0,
  },
  methods: {
    getConfirmed() {
      var that = this;
      $.ajax({
        url: "http://121.5.177.147:8090/api/c1",
        success: function (data) {
          that.confirm = data.confirm;
        },
      });
      return that.confirm;
    },

    getSuspect() {
      var that = this;
      $.ajax({
        url: "http://121.5.177.147:8090/api/c1",
        success: function (data) {
          that.suspect = data.suspect;
        },
      });
      return that.suspect;
    },

    getHeal() {
      var that = this;
      $.ajax({
        url: "http://121.5.177.147:8090/api/c1",
        success: function (data) {
          that.heal = data.heal;
        },
      });
      return that.heal;
    },

    getDead() {
      var that = this;
      $.ajax({
        url: "http://121.5.177.147:8090/api/c1",
        success: function (data) {
          that.dead = data.dead;
        },
      });
      return that.dead;
    },
  },
});
