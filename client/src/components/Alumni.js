import * as React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { CardActionArea } from '@mui/material';

import cardimg from '../images/cardimg.png';

export default function ActionAreaCard() {
    const alumni = [
        {id:1,personname:"akshay",image:"/images/dp1.png",perks:1000},
        {id:2,personname:"arjun",image:"/images/dp1.png",perks:2000},
        {id:3,personname:"akhil",image:"/images/dp1.png",perks:3000},
        {id:3,personname:"arun",image:"/images/dp1.png",perks:5400},
        
    ]
    alumni.sort((a, b) => b.perks - a.perks);
  return (
    <>
    <div
      style={{
        height: '10rem',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        textAlign: 'center',
        marginTop: '5rem',
        backgroundColor: 'rgba(110, 110, 110, 0.196)',
        
      }}
      className="heading"
    >
      <Typography variant="h4" style={{fontFamily: 'Arial',fontWeight: 'bold'}}>Marpu Alumni</Typography>
    </div>
    <div id='card' style={{ display: 'flex', justifyContent: 'center',gap: '5rem'}}>
      {alumni.map((card) => (
        <Card key={card.id} sx={{ maxWidth: 345, marginTop: '40px' }}>
          <CardActionArea>
            <CardMedia component="img" height="140" image={cardimg} alt="no image" />
            <CardContent>
              <Typography gutterBottom variant="h5" component="div">
                {card.personname}
              </Typography>
              <Typography variant="body2" color="text.secondary">
                {card.perks}
              </Typography>
            </CardContent>
          </CardActionArea>
        </Card>
      ))}
    </div>
    </>
  );
}

