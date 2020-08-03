
package entities
import java.sql.Timestamp
case class BranchKds(
	 Id : Long ,  hqId : Long ,  branchId : Long ,  name : Option[String] ,  uuId : String ,  open : Boolean  
) extends IdEntity {
}

implicit lazy val  branchKdsFormat: Format[BranchKds] = Json.format[BranchKds]