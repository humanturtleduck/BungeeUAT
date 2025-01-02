namespace Bungee_UAT
{
    partial class Form1
    {
        private System.ComponentModel.IContainer components = null;

        private Button button1;
        private Button button2;
        private Button button3;
        private Button button4;
        private Button button5;
        private Button button6;
        private ComboBox comboBox1;
        private NumericUpDown textBox1;
        private NumericUpDown textBox2;
        private CheckBox checkBox;
        private Label titleLabel;
        private Label label1;
        private Label label2;
        private Label label3;
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.Text = "Bungee UAT";
            this.Size = new System.Drawing.Size(700, 350);
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Icon= System.Drawing.Icon.ExtractAssociatedIcon(Application.ExecutablePath);
            
            this.comboBox1 = new System.Windows.Forms.ComboBox(
                
            );
            comboBox1.Items.AddRange(new object[] { "None", "Gaussian", "Gamma"});
            comboBox1.Location=new System.Drawing.Point(250, 85);
            this.Controls.Add(this.comboBox1);
            
            this.label1 = new Label
            {
                Text = "Number of random data points",
                Font = new System.Drawing.Font(System.Drawing.FontFamily.GenericSansSerif, 10.0f),
                AutoSize = true,
                Location = new System.Drawing.Point(50, 60)
            };
            
            this.Controls.Add(this.label1);
            
            this.label2 = new Label
            {
                Text = "Number of training epochs",
                Font = new System.Drawing.Font(System.Drawing.FontFamily.GenericSansSerif, 10.0f),
                AutoSize = true,
                Location = new System.Drawing.Point(50, 35)
            };
            this.Controls.Add(this.label2);
            
            this.label3 = new Label
            {
                Text = "Type of noise, intensity",
                Font = new System.Drawing.Font(System.Drawing.FontFamily.GenericSansSerif, 10.0f),
                AutoSize = true,
                Location = new System.Drawing.Point(50, 85)
            };
            this.Controls.Add(this.label3);
            
            // Title Label
            this.titleLabel = new Label
            {
                Text = "Bungee Drop Universal Approximation Theorem",
                Font = new System.Drawing.Font("Arial", 14, System.Drawing.FontStyle.Bold),
                AutoSize = true,
                Location = new System.Drawing.Point(120, 10)
            };
            this.Controls.Add(this.titleLabel);

            // TextBox1
            this.textBox1 = new NumericUpDown
            {
                Text = "Number of Training Epochs",
                Location = new System.Drawing.Point(250, 35),
                Width = 250
            };
            this.textBox1.KeyPress += (sender, e) =>
            {
                if (!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar))
                {
                    e.Handled = true;
                }
            };
            this.Controls.Add(this.textBox1);

            // TextBox2
            this.textBox2 = new NumericUpDown
            {
                Text = "Number of Random Training Values",
                Location = new System.Drawing.Point(250, 60),
                Width = 250
            };
            this.textBox2.KeyPress += (sender, e) =>
            {
                if (!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar))
                {
                    e.Handled = true;
                }
            };
            this.Controls.Add(this.textBox2);

            // CheckBox
            this.checkBox = new CheckBox
            {
                Text = "View training process",
                Location = new System.Drawing.Point(50, 110)
            };
            this.Controls.Add(this.checkBox);

            // Button1
            this.button1 = new Button
            {
                Text = "Start Training",
                Width = 200,
                Location = new System.Drawing.Point(50, 200)
            };
            this.Controls.Add(this.button1);

            // Button2
            this.button2 = new Button
            {
                Text = "Generate Data (deletes input)",
                Width = 200,
                Location = new System.Drawing.Point(400, 200)
            };
            this.Controls.Add(this.button2);

            // Button3
            this.button3 = new Button
            {
                Text = "Input data",
                Width = 200,
                Location = new System.Drawing.Point(50, 250)
            };
            this.Controls.Add(this.button3);

            // Button4
            this.button4 = new Button
            {
                Text = "View output data",
                Width = 200,
                Location = new System.Drawing.Point(400, 250)
            };
            this.Controls.Add(this.button4);

            // Button5
            this.button5 = new Button
            {
                Text = "View 3D plots",
                Width = 200,
                Location = new System.Drawing.Point(400, 150)
            };
            this.Controls.Add(this.button5);
            
            this.button6 = new Button
            {
                Text = "Change Layer Config",
                Width = 200,
                Location = new System.Drawing.Point(50, 150)
            };
            this.Controls.Add(this.button6);
        }
    }
}
