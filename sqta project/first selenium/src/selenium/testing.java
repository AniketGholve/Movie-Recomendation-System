package selenium;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.Test;

import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.ExtentTest;
import com.aventstack.extentreports.Status;
import com.aventstack.extentreports.reporter.ExtentHtmlReporter;


public class testing {
	WebDriver driver;
	
	@Test(priority=1)
	public void Signup() throws InterruptedException{
		
		System.setProperty("webdriver.chrome.driver","./drivers/chromedriver.exe");
		driver=new ChromeDriver();
		
		driver.manage().window().maximize();
		driver.get("https://www.phptravels.net/signup");
		
		Thread.sleep(2000);
		driver.findElement(By.xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[1]/div/input")).clear();
		driver.findElement(By.xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[1]/div/input")).sendKeys("Aniket");
		
		driver.findElement(By.xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[2]/div/input")).clear();
		driver.findElement(By.xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[2]/div/input")).sendKeys("Gholve");
		
		driver.findElement(By.xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[3]/div/input")).clear();
		driver.findElement(By.xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[3]/div/input")).sendKeys("9139218524");
		
		driver.findElement(By.xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[4]/div/input")).clear();
		driver.findElement(By.xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[4]/div/input")).sendKeys("aniketgholve1@gmail.com");
		
		driver.findElement(By.xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[5]/div/input")).clear();
		driver.findElement(By.xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[5]/div/input")).sendKeys("Aniket@0210");
		
		Thread.sleep(5000);
		driver.findElement(By.xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[7]/button")).click();
	
		Thread.sleep(2000);
	}

	@Test(priority=2)
	public void Login() throws InterruptedException
	{
		Thread.sleep(2000);
		//input start point 
		driver.findElement(By.xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[1]/div/input")).clear();
		driver.findElement(By.xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[1]/div/input")).sendKeys("aniketgholve1@gmail.com");
		Thread.sleep(1000);
		//input end point
		driver.findElement(By.xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[2]/div[1]/input")).clear();
		driver.findElement(By.xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[2]/div[1]/input")).sendKeys("Aniket@0210");
		Thread.sleep(1000);
	
		driver.findElement(By.xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[3]/button")).click();
	
		Thread.sleep(11000);
	
	}

	@Test(priority=3)
	public void quit_app()
	{
		driver.quit();
		
	}
}
