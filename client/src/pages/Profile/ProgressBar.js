import React from 'react';
import { Chart } from 'react-google-charts';
import Button from '@mui/material/Button';
import { Typography } from '@mui/material';
import { useState } from 'react';
import Certificate from './Certificate';

const ProgreeBar = () => {
//  function handleClick() {
//     window.location.href = 
//  }

  var isButtonEnabled = false; // Your boolean variable
  var threshold = 20000;
  const [funds,setFunds] = useState(3000);
  const gaugeData = [
    ['Label', 'Value'],
    ['Progress', funds],
  ]; // Sample data for the gauge chart
  if(funds >= threshold){
    isButtonEnabled = true;
  }

  return (
    <div >
      <Typography  variant="h6"  style={{ fontFamily: 'Arial', fontWeight: 'bold', marginTop: '2rem' }}>
                        Progress chart
                    </Typography>
      <div >
        <Chart
          width={600}
          height={140}
          chartType="Gauge"
          loader={<div>Loading Chart</div>}
          data={gaugeData}
          options={{
            redFrom: 0,
            redTo: 100,
            yellowFrom: 75,
            yellowTo: 90,
            minorTicks: 5,
          }}
          rootProps={{ 'data-testid': '1' }}
        />
        
      </div>
      <div style={{marginTop:'2rem',}}>
        <Button onSubmit={handleclick} disabled={!isButtonEnabled} variant="contained">
          Certificate
        </Button>
      </div>
      <div>
            Perks : 50 points
            Goodies : T-shirt from the Marpu Foundation
        </div>
    </div>

  );
};

export default ProgreeBar;
