import React from "react";
import Typography from '@mui/material/Typography';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';

const Orientation = () => {

    const handleClick = () => {
        window.location.href = "https://zoom.us";
      }

    return (
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh'}}>
            <Card sx={{ maxWidth: 500, backgroundColor: '#FFFDD0', borderRadius: '10px', boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)' }}>
                <CardContent>
                    <Typography variant="h4" textAlign="center" style={{ fontFamily: 'Arial', fontWeight: 'bold', marginTop: '2rem' }}>
                        Orientation
                    </Typography>
                    <div
                        id='descript'
                        style={{
                            margin: '2rem',
                            textAlign: 'start',
                        }}
                    >
                        Our volunteers are the shining stars! Lighting up daily with their
                        selfless acts of heroism. As a Marpu Foundation intern, you'll have the
                        opportunity to gain valuable skills and experience while working on
                        projects and campaigns that align with your interests and passions. You
                        will have a chance to support our efforts to create a more socially
                        responsible society, by working in the field or online as per feasibility.
                        Contribute to the Marpu Foundation mission by volunteering your time and
                        skills or gaining hands-on experience through an internship opportunity.
                        For institutional or university partnerships, please email us at
                        contact@marpu.org with your details and proposal.
                    </div>
                    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', }}>
                        <Button variant="contained" onClick={handleClick} >Zoom Link</Button>
                    </div>
                </CardContent>
            </Card>
        </div>
    );
};

export default Orientation;
