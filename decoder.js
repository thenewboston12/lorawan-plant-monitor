function decodeUplink(input) {
  var data = {};
  var events = {
    1: "setup",
    2: "interval",
    3: "motion",
    4: "button"
  };
  data.event = events[input.fPort];
  // to function
  var measurements = [];
  for (let i = 0; i < 3; i++){
    var bits = (input.bytes[0+i*4] << 24) | (input.bytes[1+i*4] << 16) |(input.bytes[2+i*4] << 8) |(input.bytes[3+i*4]);
    measurements.push(decodeFloat(bits));
  }


  data.airtemp = measurements[0]
  data.soiltemp = measurements[1]
  data.light  = measurements[2];
  data.temperature = 24

  var warnings = [];

  return {
    data: data,
    warnings: warnings
  };
}

function decodeFloat( bits){
  var sign = (bits >>> 31 === 0) ? 1.0 : -1.0;
  var e = bits >>> 23 & 0xff;
  var m = (e === 0) ? (bits & 0x7fffff) << 1 : (bits & 0x7fffff) | 0x800000;
  var f = sign * m * Math.pow(2, e - 150)
  return f
}
